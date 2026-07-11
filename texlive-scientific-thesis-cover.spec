%global tl_name scientific-thesis-cover
%global tl_revision 79352

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.1.0
Release:	%{tl_revision}.1
Summary:	Provides cover page and affirmation at the end of a thesis
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/scientific-thesis-cover
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scientific-thesis-cover.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scientific-thesis-cover.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scientific-thesis-cover.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Institutions require a cover page and an affirmation at the end of a
thesis. This package provides both.

